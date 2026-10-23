# R185VER

## Descrição

Orçamento Individual - Definições da Versão

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| DesRed | String(030) | Sim | Descrição reduzida da versão do orçamento |
| SitOrc | Number(001,0) | Sim | Situação do cálculo do orçamento(Simulado/Oficial) |
| PerRev | String(001) | Sim | Permite cadastrar outras revisões |
| DesDet | String(500) | Sim | Descrição detalhada da versão do orçamento |

---

## Chave Primária

- NumEmp
- AnoBas
- VerOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185VER_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

