function BandwidthRate({ rate }) {
  return (
    <div style={styles.card}>
      <h2>Bandwidth Rate</h2>
      <h1>{rate?.toFixed(2) || 0} B/s</h1>
    </div>
  );
}

const styles = {
  card: {
    padding: "15px",
    backgroundColor: "#1e293b",
    borderRadius: "10px",
    marginBottom: "10px",
    color: "white",
  },
};

export default BandwidthRate;
