import React from "react";
import PropTypes from "prop-types";
import Device from "./Device";

export default class DevicePanel extends React.Component {
  static propTypes = {
    clickHandler: PropTypes.func,
  };

  handleClick = (deviceName) => {
    this.props.clickHandler(deviceName);
  };

  render() {
    return (
      <div className="component-button-panel">
        <div>
          <Device name="D1" clickHandler={this.handleClick} />
          <Device name="D2" clickHandler={this.handleClick} />
          <Device name="D3" clickHandler={this.handleClick} />
          <Device name="D4" clickHandler={this.handleClick} orange />
        </div>
        <div>
          <Device name="D5" clickHandler={this.handleClick} />
          <Device name="D6" clickHandler={this.handleClick} />
          <Device name="D7" clickHandler={this.handleClick} />
          <Device name="D8" clickHandler={this.handleClick} orange />
        </div>
        <div>
          <Device name="D9" clickHandler={this.handleClick} />
          <Device name="D10" clickHandler={this.handleClick} />
          <Device name="D11" clickHandler={this.handleClick} />
          <Device name="D12" clickHandler={this.handleClick} orange />
        </div>
        <div>
          <Device name="D13" clickHandler={this.handleClick} />
          <Device name="D14" clickHandler={this.handleClick} />
          <Device name="D15" clickHandler={this.handleClick} />
          <Device name="D16" clickHandler={this.handleClick} orange />
        </div>
      </div>
    );
  }
}
