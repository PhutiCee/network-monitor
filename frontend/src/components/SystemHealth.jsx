function SystemHealth({ data }) {
  return (
    <div style={styles.card}>
      <h3>System Health</h3>

      <div>Connections: {data.connections}</div>
      <div>Protocols: {Object.keys(data.protocols || {}).length}</div>

      <div style={styles.status}>
        {data.connections > 0 ? "🟢 Healthy" : "🟡 Idle"}
      </div>
    </div>
  );
}

const styles = {
  card: {
    backgroundColor: "#111827",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "10px",
    border: "1px solid #1f2937",
  },
  status: {
    marginTop: "10px",
    fontWeight: "bold",
  },
};

export default SystemHealth;
