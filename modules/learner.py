import learner_protocol_pb2
import agent_protocol_pb2
import sys


class Learner:
    def __init__(self):
        self.read_protocol("learner")
        self.read_protocol("agent")

    def compile_protocols(self):
        # compile: $ protoc -I=./ --cpp_out=../../../core/modules/example ./learner.proto 
        # compile: $ protoc -I=./ --python_out=./ ./learner.proto

        # And inside core/modules/example:

        # compile: $ protoc -I=./ --python_out=../../../tools/SoccerAcademy/modules/  ./agent.proto
        # compile: $ protoc -I=./ --cpp_out=./ ./agent.proto
        pass

    

    # Reads message in .proto
    def read_protocol(self, protocol: str):
        if protocol == "learner":
            self.learner_protocol = learner_protocol_pb2.Learner()
        elif protocol == "agent":
            self.agent_protocol = agent_protocol_pb2.Agent()

        # Read the existing learner protocol.
        try:
            f = open(protocol, "rb")
            self.protocol.ParseFromString(f.read())
            f.close()
        except IOError:
            print(protocol + ": Could not open file.  Creating a new one.")


    # Writes message in .proto 
    def write_learner_protocol(self, new_task: str, action: float):
        learner_protocol = self.learner_protocol.add()

        if new_task == "START":
            learner_protocol.task = learner_protocol_pb2.Learner.START
        elif new_task == "RESET":
            learner_protocol.task = learner_protocol_pb2.Learner.RESET
        elif new_task == "END":
            learner_protocol.task = learner_protocol_pb2.Learner.END
        else:
            print("Unknown phone type; leaving as default value.")
