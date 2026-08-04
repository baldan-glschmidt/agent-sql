# E440DAC

## Descrição

Compras - Notas Fiscais de Entrada - Dias de Aquisição de Cana

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| DiaAqi | Number(002,0) | Não | Dia da Aquisição da Cana |
| QtdAqi | Number(015,4) | Sim | Quantidade recebida de Cana no Dia |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- DiaAqi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DAC_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440DAC_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

