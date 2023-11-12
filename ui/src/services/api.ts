import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://192.168.0.173:5000',
    timeout: 10_000,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default apiClient;


export const getDevices = () => {
    return apiClient.get('get-devices');
};

export const getTasks = () => {
    return apiClient.get('get-tasks');
};

export const executeTask = (name: string) => {
    return apiClient.post('execute-task', { 'name': name });
};

export const getProperty = (device: string, property: string) => {
    return apiClient.get(`get-property?device=${device}&property=${property}`);
};

export const setProperty = (device: string, property: string, value: string) => {
    return apiClient.post('set-property', {
        'device': device,
        'property': property,
        'value': value,
    });
};
