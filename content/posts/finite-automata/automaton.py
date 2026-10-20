# from typing import Set
# from abc import ABC, abstractmethod


# class FiniteAutomaton(ABC):
#     def __init__(
#         self,
#         states: set[str],
#         start: str,
#         accepts: set[str],
#         alphabet: set[str],
#     ):
#         self.states = states
#         self.start = start
#         self.accepts = accepts
#         self.alphabet = alphabet

#     @abstractmethod
#     def transition(self, state: str, input: str) -> str:
#         pass

#     def is_accept(self, state: str) -> bool:
#         return state in self.accepts

#     def accept_empty(self) -> bool:
#         return self.start in self.accepts

#     def draw_transition_table(self):
#         print("  |", end="")
#         for i in self.alphabet:
#             print(f"{i}", end="\t")

#         print()

#         print("-" * len(self.alphabet))
#         for i in self.states:
#             for j in self.alphabet:
#                 print(f"{i} | {self.transition(i, j)}", end="\t")
#             print()


# class M1(FiniteAutomaton):
#     def __init__(self):
#         super().__init__(
#             states=["q1", "q2", "q3"],
#             start="q2",
#             accepts=["q2"],
#             alphabet=["0", "1"],
#         )

#     def transition(self, state: str, input: str) -> str:
#         assert input in self.alphabet
#         assert state in self.states
