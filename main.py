import sys
from api.src.server.instance import server
from api.src.controller import (
    CreateTransaction, 
    GetMemoryPoolTransactions,
    GetChain,
    MineBlock,
    ResolveConflicts,
    CreateNode
)


port = sys.argv[1] if len(sys.argv) > 1 else 5000
server.run(port=port)