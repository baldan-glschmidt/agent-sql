# R584PLA

## Descrição

Manutenção do Inventário de Riscos - GHEs - Planos de Ação

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| NumEmp | Number(004,0) | Não | Código da Empresa do Plano de Ação |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPRA
- CodGHE
- NumEmp
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R584PLA_006

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

