import React from "react";

class ClientBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: props.data,
      backgroundColor: "white",
    };
    this.handleDetection = this.handleDetection.bind(this);
  }
  handleDetection() {
    const suspicious = this.state.item.suspicious;
    if (suspicious === "true") {
      this.setState({ backgroundColor: "red" });
    } else {
      this.setState({ backgroundColor: "white" });
    }
  }

  render() {
    return (
      <div
        className="box"
        id={this.props.id}
        style={{
          backgroundColor: this.state.backgroundColor,
          width: "100px",
          height: "100px",
        }}
      >
        {this.state.data.mainType}
      </div>
    );
  }
}
export default ClientBox;
