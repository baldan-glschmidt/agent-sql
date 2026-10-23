# R053CSE

## Descrição

RAIS - Contribuições Sindicais da Empresa

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpArq | Number(004,0) | Não | Código da Empresa no Arquivo |
| AnoBas | Number(004,0) | Não | Ano Base da Rais |
| FilArq | Number(006,0) | Não | Código da Filial no Arquivo |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| TipCsi | Number(001,0) | Não | Tipo Contribuição |
| ValCon | Number(011,2) | Sim | Valor Contribuição |
| OriMov | String(001) | Sim | Origem do Registro |

---

## Chave Primária

- EmpArq
- AnoBas
- FilArq
- CodSin
- TipCsi

---

## Índices

### R053CSEIndice2

**Tipo:** Não unico

Campos:
- AnoBas
- OriMov

---

## Relacionamentos

### IR_R053CSE_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| EmpArq | NumEmp |
| FilArq | CodFil |

### IR_R053CSE_003

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

