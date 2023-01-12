import "./App.css";
import React from "react";
import ClientBox from "./components/ClientBox";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {
          deviceId: "10:00:00:01",
          timeStamp: "2023/07/01,08:09:21",
          suspicious: "true",
          mainType: "face",
          subType: "no-face",
        },
        {
          deviceId: "10:00:00:01",
          timeStamp: "2023/07/01,08:09:21",
          suspicious: "false",
          mainType: "lip",
          subType: "none",
        },
        {
          deviceId: "10:00:00:02",
          timeStamp: "2023/07/01,08:09:21",
          suspicious: "true",
          mainType: "head",
          subType: "none",
        },
      ],
    };
  }

  render() {
    return (
      <div>
        {this.state.data.map((item) => (
          <ClientBox key={item.deviceId} id={item.deviceId} data={item} />
        ))}
      </div>
    );
  }
}

export default App;
