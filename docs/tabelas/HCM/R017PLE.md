# R017PLE

## Descrição

Estrutura de Postos - Plano de Vagas - Empresas

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| PlnAti | String(001) | Sim | Define se o plano de vagas está ativo para esta empresa |

---

## Chave Primária

- EstPos
- CodPlv
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017PLE_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

