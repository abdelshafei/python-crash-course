from enum import Enum

class State(Enum):
    inactive = 0
    active = 1 
print(State.active.value) #1
print(State(1)) #State.active
print(State['active']) #State.active
print(State['active'].value) #1
print(list(State)) #[<State.inactive: 0>, <State.active: 1>] 
print(len(State)) #2
