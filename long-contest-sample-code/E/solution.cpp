#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

string raw_all_pkmn_types = "Normal Fighting Flying Poison Ground Rock Bug Ghost Steel Fire Water Grass Electric Psychic Ice Dragon Dark Fairy";
string raw_matchup_table = "\
1	1	1	1	1	0.5	1	0	0.5	1	1	1	1	1	1	1	1	1   \
2	1	0.5	0.5	1	2	0.5	0	2	1	1	1	1	0.5	2	1	2	0.5 \
1	2	1	1	1	0.5	2	1	0.5	1	1	2	0.5	1	1	1	1	1   \
1	1	1	0.5	0.5	0.5	1	0.5	0	1	1	2	1	1	1	1	1	2   \
1	1	0	2	1	2	0.5	1	2	2	1	0.5	2	1	1	1	1	1   \
1	0.5	2	1	0.5	1	2	1	0.5	2	1	1	1	1	2	1	1	1   \
1	0.5	0.5	0.5	1	1	1	0.5	0.5	0.5	1	2	1	2	1	1	2	0.5 \
0	1	1	1	1	1	1	2	1	1	1	1	1	2	1	1	0.5	1   \
1	1	1	1	1	2	1	1	0.5	0.5	0.5	1	0.5	1	2	1	1	2   \
1	1	1	1	1	0.5	2	1	2	0.5	0.5	2	1	1	2	0.5	1	1   \
1	1	1	1	2	2	1	1	1	2	0.5	0.5	1	1	1	0.5	1	1   \
1	1	0.5	0.5	2	2	0.5	1	0.5	0.5	2	0.5	1	1	1	0.5	1	1   \
1	1	2	1	0	1	1	1	1	1	2	0.5	0.5	1	1	0.5	1	1   \
1	2	1	2	1	1	1	1	0.5	1	1	1	1	0.5	1	1	0	1   \
1	1	2	1	2	1	1	1	0.5	0.5	0.5	2	1	1	0.5	2	1	1   \
1	1	1	1	1	1	1	1	0.5	1	1	1	1	1	1	2	1	0   \
1	0.5	1	1	1	1	1	2	1	1	1	1	1	2	1	1	0.5	0.5 \
1	2	1	0.5	1	1	1	1	0.5	0.5	1	1	1	1	1	2	2	1   \
";

class Pokemon {
  public:
    static void initialize() {
        stringstream ss;

        ss << raw_all_pkmn_types;
        all_pkmn_types = vector<string>(TYPE_COUNT);
        for (int i = 0; i < TYPE_COUNT; i++) {
            ss >> all_pkmn_types[i];
        }

        get_type_index = map<string, int>();
        for (int i = 0; i < TYPE_COUNT; i++) {
            get_type_index[all_pkmn_types[i]] = i;
        }

        ss.clear();
        ss << raw_matchup_table;
        matchup_table = vector<vector<double>>(TYPE_COUNT);
        for (int i = 0; i < TYPE_COUNT; i++) {
            matchup_table[i] = vector<double>(TYPE_COUNT);
            for (int j = 0; j < TYPE_COUNT; j++) {
                ss >> matchup_table[i][j];
            }
        }
    }

    Pokemon(vector<string> types) {
        this->types = types;
        sort(this->types.begin(), this->types.end());
    }

    double attacked_by(string attacking_type) const {
        double ans = 1;
        for (const string& defending_type: this->types) {
            ans *= matchup_table[get_type_index[attacking_type]][get_type_index[defending_type]];
        }
        return ans;
    }

    string output_types() const {
        string ans = "";
        for (int t = 0; t < this->types.size(); t++) {
            if (t != 0) {
                ans += '/';
            }
            ans += this->types[t];
        }
        return ans;
    }
  
    static const int TYPE_COUNT = 18;
    static vector<string> all_pkmn_types;
    static vector<vector<double>> matchup_table;
    static map<string, int> get_type_index;
    const static vector<double> possible_results;

  private:
    vector<string> types;
};
vector<string> Pokemon::all_pkmn_types;
vector<vector<double>> Pokemon::matchup_table;
map<string, int> Pokemon::get_type_index;
const vector<double> Pokemon::possible_results = {4, 2, 1, 0.5, 0.25, 0};

const int MAGIC_LIMIT = 5;
struct DecisionTree {
    map<double, DecisionTree*> branches;
    string query_type;

    ~DecisionTree() {
        for (auto[key, value] : branches) {
            delete value;
        }
    }
};

DecisionTree* generate_decision_tree(
    const vector<Pokemon>& candidates,
    set<string>& used_attacks
) {
    if (candidates.empty()) {
        return new DecisionTree{
            map<double, DecisionTree*>(),  // empty
            "Liar!"
        };
    }
    if (candidates.size() == 1) {
        return new DecisionTree{
            map<double, DecisionTree*>(),  // empty
            candidates[0].output_types()
        };
    }
    if (used_attacks.size() == MAGIC_LIMIT) {
        return nullptr; // cut off the branch here
    }
    
    for (const string& attacking_type : Pokemon::all_pkmn_types) {
        if (used_attacks.find(attacking_type) == used_attacks.end()) {
            used_attacks.insert(attacking_type);
            
            map<double, vector<Pokemon>> partitions;
            for (const double result : Pokemon::possible_results) {
                partitions[result] = vector<Pokemon>();
            }
            for (const Pokemon& pkmn : candidates) {
                partitions[pkmn.attacked_by(attacking_type)].push_back(pkmn);
            }

            bool viable_tree = true;
            DecisionTree* possible_tree = new DecisionTree();
            possible_tree->query_type = attacking_type;
            for (auto&[result, partition] : partitions) {
                possible_tree->branches[result] = generate_decision_tree(
                    partition,
                    used_attacks
                );
                if (possible_tree->branches[result] == nullptr) {
                    viable_tree = false;
                    break;
                }
            }
            used_attacks.erase(attacking_type);

            if (viable_tree) {
                return possible_tree;
            } else {
                delete possible_tree;
            }
        }
    }

    return nullptr;
}

double query(string attacking_type) {
    cout << "ATTACK " << attacking_type << endl;
    double res; cin >> res;
    return res;
}

int main() {
    Pokemon::initialize();

    vector<Pokemon> all_pkmn_type_combos;
    for (int i = 0; i < Pokemon::TYPE_COUNT; i++) {
        all_pkmn_type_combos.push_back(Pokemon({Pokemon::all_pkmn_types[i]}));
    }
    for (int i = 0; i < Pokemon::TYPE_COUNT; i++) {
        for (int j = i+1; j < Pokemon::TYPE_COUNT; j++) {
            all_pkmn_type_combos.push_back(Pokemon({
                Pokemon::all_pkmn_types[i],
                Pokemon::all_pkmn_types[j]
            }));
        }    
    }
    
    set<string> used_attacks;
    DecisionTree* root = generate_decision_tree(
        all_pkmn_type_combos,
        used_attacks
    );

    int T; cin >> T;
    while (T--) {
        DecisionTree* current_node = root;
        while (!current_node->branches.empty()) {
            current_node = current_node->branches[query(current_node->query_type)];
        }

        cout << "ANSWER " << current_node->query_type << endl;

        string verify; cin >> verify;
        assert(verify == "YES");
    }
    return 0;
}