import React, { useState, useEffect } from 'react';
import { fetchNumTickets } from '../services'
import { Card } from 'react-bootstrap';

export const NumTickets = ({ }) => {
    const [data, setData] = useState({ id: null, fabricante: null, modelo: null, quantidade_chamados: null });

    useEffect(async () => {
        const result = await fetchNumTickets()

        setData(result);
    }, []);

    return (
        <div className="col m4">
            <Card className="text-center">
                <Card.Header>Equipamento com mais chamados</Card.Header>
                <Card.Body>
                    <Card.Text>
                        <div>id: {data.id}</div>
                        <div>Fabricante: {data.fabricante}</div>
                        <div>Modelo: {data.modelo}</div>
                        <div>Quantidade de chamados: {data.quantidade_chamados}</div>
                    </Card.Text>
                </Card.Body>
            </Card>
        </div>

    )
};
