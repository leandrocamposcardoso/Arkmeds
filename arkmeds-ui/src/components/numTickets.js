import React, { useState, useEffect } from 'react';
import { fetchNumTickets } from '../services'

export const NumTickets = ({ }) => {
    const [data, setData] = useState({id: null, fabricante:null, modelo: null, quantidade_chamados: null});

    useEffect(async () => {
        const result = await fetchNumTickets()

        setData(result);
    }, []);

    return (
        <div>
            <h3>Equipamento com mais chamados</h3>
            <div>id: {data.id}</div>
            <div>Fabricante: {data.fabricante}</div>
            <div>Modelo: {data.modelo}</div>
            <div>Quantidade de chamados: {data.quantidade_chamados}</div>

        </div>

    )
};
