import React, { useState, useEffect } from 'react';
import { fetchMaxEquipment } from '../services'
import { Card } from 'react-bootstrap';

export const NumEquipments = ({ }) => {
    const [data, setData] = useState({ id: null, nome: null, quantidade_equipamentos: null });

    useEffect(async () => {
        const result = await fetchMaxEquipment()

        setData(result);
    }, []);

    return (
        <div className="col m4">
            <Card className="text-center">
                <Card.Header>Proprietário com mais equipamentos</Card.Header>
                <Card.Body>
                    <Card.Text>
                        <div>id: {data.id}</div>
                        <div>nome: {data.nome}</div>
                        <div>Quantidade de equipamentos: {data.quantidade_equipamentos}</div>
                    </Card.Text>
                </Card.Body>
            </Card>
        </div>

    )
};
