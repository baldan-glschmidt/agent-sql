# R088SIN

## Descrição

Sinistros de Veículos

---

## Resumo

- Campos: 19
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatSin | Date | Não | Data do Sinistro do Veículo |
| HorSin | Number(005,0) | Não | Hora do Sinistro do Veículo |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| EmpCon | Number(004,0) | Sim | Empresa do Colaborador Condutor do Veículo |
| TipCon | Number(001,0) | Sim | Tipo de Condutor da Frota |
| CadCon | Number(009,0) | Sim | Cadastro do Colabolador Condutor do Veículo |
| DesSin | String(1500) | Sim | Descrição do Sinistro do Veículo |
| ValSin | Number(011,2) | Sim | Valor para Reparo do Sinistro do Veículo |
| QtdPon | Number(002,0) | Sim | Quantidade de Pontos para o Condutor do Veículo |
| SitVei | Number(003,0) | Sim | Situação do Veículo |
| ForRee | Number(001,0) | Sim | Sinistro será Reembolsado por |
| TipTpa | Number(001,0) | Sim | Tipo de Via em que Ocorreu o Acidente |
| TemVit | String(001) | Sim | Houve Vítima (S/N) |
| TemPrd | String(001) | Sim | Houve Perda Total do Veículo (S/N) |
| TipSin | Number(002,0) | Sim | Tipo  de Acidente |
| EndRua | String(040) | Sim | Endereço onde ocorreu o Acidente |
| SinEvi | String(001) | Sim | Sinistro poderia ter sido Evitável (S/N) |

---

## Chave Primária

- PlaVei
- DatSin
- HorSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088SIN_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

