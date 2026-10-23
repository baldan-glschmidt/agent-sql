# R110IMP

## Descrição

Impedanciômetros

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodImp | Number(003,0) | Não | Código do Impedanciômetro |
| DesImp | String(030) | Sim | Descrição Impedanciômetro |
| FabImp | String(040) | Sim | Fabricante do Audiometro |
| MldImp | String(030) | Sim | Modelo do Impedanciômetro |
| TemAfe | Number(002,0) | Sim | Tempo para Aferição em Meses |
| TemCal | Number(002,0) | Sim | Tempo para Calibragem em Meses |
| NroSer | String(030) | Sim | Número de série do aparelho |
| MedCE1 | Number(003,2) | Sim | 1a.Medida mais alta da complacência estática |
| MedCE2 | Number(003,2) | Sim | 2a.Medida mias alta da complacência estática |
| MedCE3 | Number(003,2) | Sim | 3a.Medida mais alta da complacência estática |
| MedCE4 | Number(003,2) | Sim | 4a.Medida mais alta da complacência estática |
| MedCE5 | Number(003,2) | Sim | 5a.Medida mais alta da complacência estática |
| MedCE6 | Number(003,2) | Sim | 6a.Medida mais alta da complacência estática |
| MedCE7 | Number(003,2) | Sim | 7a.Medida mais alta da complacência estática |
| MedCE8 | Number(003,2) | Sim | 8a.Medida mais alta da complacência estática |
| MedCE9 | Number(003,2) | Sim | 9a.Medida mais alta da complacência estática |
| MedC10 | Number(003,2) | Sim | 10a.Medida mais alta da complacência estática |
| MedC11 | Number(003,2) | Sim | Medida mais baixa da complacência estática |

---

## Chave Primária

- NumEmp
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110IMP_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

