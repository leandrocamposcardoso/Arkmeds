import React, { useState, useEffect } from 'react';
import { fetchMaxEquipment } from '../services'

export const NumEquipments = ({ }) => {
    const [data, setData] = useState({id: null, nome:null, quantidade_equipamentos: null});

    useEffect(async () => {
        const result = await fetchMaxEquipment()

        setData(result);
    }, []);

    return (
        <div>
            <h3>Proprietario que possui mais equipamentos</h3>
            <div>id: {data.id}</div>
            <div>nome: {data.nome}</div>
            <div>Quantidade de equipamentos: {data.quantidade_equipamentos}</div>

        </div>

    )
};
