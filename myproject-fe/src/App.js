import React, { Component } from 'react';
import './App.css';
import axios from 'axios';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      pollingDelay: 3000,
    }
  }

  componentDidMount() {
    this.refreshData();
    this.interval = setInterval(this.refreshData, this.state.pollingDelay);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  refreshData = async () => {
    const response = axios.get("/app/");
    const data = (await response).data[0]["data"];
    this.setState({ data });
  };

  render() {
    const { data } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <table className="table table-dark">
            <colgroup>
              <col />
              <col />
              <col />
              <col />
              <col />
              <col />
              <col />
              <col />
              <col />
            </colgroup>
            <thead>
              <tr>
                <th scope='col'>#</th>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
                <th scope="col">1h</th>
                <th scope="col">24h</th>
                <th scope="col">7d</th>
                <th scope="col">Market Cap</th>
                <th scope="col">Volume(24h)</th>
                <th scope="col">Circulating Supply</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => {
                return (
                  <tr key={index + 1}>
                    <td>{index + 1}</td>
                    <td>{item.name}</td>
                    <td>{item.price}</td>
                    <td>{item.change["1h"]}</td>
                    <td>{item.change["24h"]}</td>
                    <td>{item.change["7d"]}</td>
                    <td>{item.mcap}</td>
                    <td>{item.volume.amt}</td>
                    <td>{item.c_supply}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </header>
      </div>
    );
  }
}

export default App;
