
import { API_HOST } from './consts';
import axios from 'axios';

export const fetchMaxEquipment= async (params) => {
    const res = await axios.get(`${API_HOST}/equipamentos/proprietario/num_equipments`, { params });
    return res.data;
};


export const fetchNumTickets= async (params) => {
    const res = await axios.get(`${API_HOST}/equipamentos/equipamento/num_tickets`, { params });
    return res.data;
};
export const fetchAllTickets= async (page) => {
    const res = await axios.get(`${API_HOST}/equipamentos/chamado_equipamento?page=${page}`);
    return res.data;
};
