# R126CIN

## Descrição

Candidatos p/ Integração

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Codigo Requisicao |
| SeqCan | Number(005,0) | Não | Sequência dos Candidatos Aprovados p/ Admissão |
| EmpRqu | Number(004,0) | Sim | Código de Empresa da Requisição |
| TipCan | Number(001,0) | Sim | Tipo do Candidato |
| NumCan | Number(007,0) | Sim | Cadastro Candidatos |
| NumEmp | Number(004,0) | Sim | C¢digo da Empresa |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| DatAdm | Date | Sim | Data admissao |

---

## Chave Primária

- CodRqu
- SeqCan

---

## Índices

### R126CINIndice2

**Tipo:** Não unico

Campos:
- CodRqu

---

## Relacionamentos

### IR_R126CIN_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| EmpRqu | NumEmp |

