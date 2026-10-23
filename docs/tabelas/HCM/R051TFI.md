# R051TFI

## Descrição

Rendimentos Informe/DIRF - Totalizador por Filial

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| CodFil | Number(006,0) | Não | Código da Filial |
| DesInf | String(040) | Sim | Descrição Totalizador para Informe |

---

## Chave Primária

- NumEmp
- TabEve
- CodTot
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051TFI_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

