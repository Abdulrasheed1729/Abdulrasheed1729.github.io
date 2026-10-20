#include <functional>
#include <unordered_set>

template <typename T> struct FiniteAutomaton {

  FiniteAutomaton(std::unordered_set<T> states, std::unordered_set<T> alphabet,
                  T start_state, std::unordered_set<T> accept_states,
                  std::function<T(T, T)> transition) {
    this->states = states;
    this->start_state = start_state;
    this->transition = transition;
    this->alphabet = alphabet, this->accept_states = accept_states;
  }

  const std::unordered_set<T> &getStates() const { return states; }
  const std::unordered_set<T> &getAlphabet() const { return alphabet; }
  const T &getStartState() const { return start_state; }
  const std::unordered_set<T> &getAcceptStates() const { return accept_states; }

private:
  std::function<T(T, T)> transition;
  std::unordered_set<T> states;
  std::unordered_set<T> alphabet;
  T start_state;
  std::unordered_set<T> accept_states;
};
