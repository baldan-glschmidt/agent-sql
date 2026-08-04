# E140IAA

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Informações adicionais do modal aéreo

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIaa | Number(004,0) | Não | Sequência de informação de manuseio |
| CodIma | Number(002,0) | Sim | Código da informação do manuseio |
| CodImp | String(010) | Sim | Informação do código Interline Message Procedure (IMP) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIaa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140IAA_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140IAA_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

