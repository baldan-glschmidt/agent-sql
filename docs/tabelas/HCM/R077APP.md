# R077APP

## Descrição

Avaliação de Performance - Pesos

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| PesAv1 | Number(002,0) | Sim | Peso da Autoavaliação |
| PesAv2 | Number(002,0) | Sim | Peso da Avaliação dos Superiores |
| PesAv3 | Number(002,0) | Sim | Peso da Avaliação dos Subordinados |
| PesAv4 | Number(002,0) | Sim | Peso da Avaliação dos Cargos Pares |
| PesAv5 | Number(002,0) | Sim | Peso da Avaliação dos Clientes |
| PesAv6 | Number(002,0) | Sim | Peso da Avaliação dos Fornecedores |
| PesAv7 | Number(002,0) | Sim | Peso da Avaliação dos Instrutores |
| PesAv8 | Number(002,0) | Sim | Peso da avaliação de consenso |
| PerExc | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - % Excelência |
| PerPfm | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - % Performance |
| PerDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - % Domínio |
| PerApf | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - % Aperfeiçoamento |
| PerFor | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - % Formação |
| NotExc | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Excelência |
| NotPfm | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Performance |
| NotDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Domínio |
| NotApf | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Aperfeiçoamento |
| NotFor | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Formação |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077APP_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

