function Connections({ count }) {
  return (
    <div style={styles.connection}>
      <h2>Active Connections</h2>
      <h1>{count}</h1>
    </div>
  );
}

const styles = {
  connection: {
    backgroundColor: "#111827",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "20px",
    border: "1px solid #1f2937",
  },
};

export default Connections;
