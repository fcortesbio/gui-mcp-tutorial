# gui-mcp-tutorial/env.sh
export BRD_API_KEY=$(grep BRD_API_KEY secrets.txt | cut -d = -f2 | tr -d '"')
