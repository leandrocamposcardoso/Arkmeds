import React, { useState, useEffect } from 'react';
import { fetchAllTickets } from '../services'

import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import Spinner from 'react-bootstrap/Spinner'

export const TicketsTable = ({ }) => {
    const [page, setPage] = useState(1);
    const [equipments, setEquipments] = useState([]);
    const [totalSize, setTotalSize] = useState(0);
    const [sizePerPage, setSizePerPage] = useState(10);
    const [fetching, setFetching] = useState(true);

    const handleFetch = async(page) => {
      fetchAllTickets(page)
        .then((data) => {
          setTotalSize(data.count)
          setSizePerPage(data.per_page)
          setEquipments(
            data.results.map(element => (
            {
                id: element.id,
                numero: element.numero,
                apelido: element.equipamento.proprietario.apelido,
            })
          ))
          setFetching(false);
        })
    }

    useEffect(() => {
      setFetching(true);
        handleFetch(page);
    }, [page]);

    const columns = [
        { dataField: 'id', text: 'Id', sort: true },
        { dataField: 'numero', text: 'numero', sort: true },
        { dataField: 'apelido', text: 'apelido', sort: true }
    ];

    const defaultSorted = [{
        dataField: 'id',
        order: 'desc'
    }];


    const pagination = paginationFactory({
        page,
        totalPages: 5,
        setTotalPages: 100,
        sizePerPage,
        lastPageText: '>>',
        firstPageText: '<<',
        nextPageText: '>',
        prePageText: '<',
        showTotal: true,
        totalSize,
        sizePerPageList: [ {text: sizePerPage, value: sizePerPage}],
        onPageChange: function (page) {
            setPage(page)
        },
    });

    const mystyle = {
      marginTop: "20px"

    };

    return (
      <div style={mystyle}>
        {fetching ?
          (<Spinner animation="border" />)
          :
          (<BootstrapTable
              remote
              bootstrap4
              keyField='id'
              data={equipments}
              columns={columns}
              defaultSorted={defaultSorted}
              pagination={pagination}
              onTableChange={()=>{}}
          />)
        }
      </div>

    )
};
