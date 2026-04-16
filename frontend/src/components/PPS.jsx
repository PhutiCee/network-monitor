function PPS({ value }) {
  return (
    <div style={styles.card}>
      <h2>Packets / Second</h2>
      <h1>{value?.toFixed(2) || 0}</h1>
    </div>
  );
}

const styles = {
  card: {
    padding: "15px",
    backgroundColor: "#0f172a",
    borderRadius: "10px",
    marginBottom: "10px",
    color: "white",
  },
};

export default PPS;
