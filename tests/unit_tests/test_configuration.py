from langgraph.pregel import Pregel

from agent.graph import graph


def test_placeholder() -> None:
    # TODO: You can add actual unit tests
    # for your graph and other logic here.
    print(f"Graph: {graph.name}")
    assert isinstance(graph, Pregel)


def test_graph_name() -> None:
    assert graph.name == "Demo Agent"


def test_graph_has_agent_and_tools_nodes() -> None:
    assert {"agent", "tools"}.issubset(graph.nodes.keys())
