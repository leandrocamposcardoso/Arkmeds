import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.css';
import 'react-bootstrap-table2-paginator/dist/react-bootstrap-table2-paginator.min.css';

import {NumEquipments} from './components/numEquipments'
import {NumTickets} from './components/numTickets'
import {TicketsTable} from './components/ticketsTable'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Arkmeds Gerenciamento de Equipamentos</h1>
        <NumEquipments></NumEquipments>
        <br />
        <NumTickets></NumTickets>
        <br />
        <TicketsTable></TicketsTable>
      </header>
    </div>
  );
}

export default App;
