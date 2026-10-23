# R016TAB

## Descrição

Reestruturação Organograma - Tabelas de Usuário

---

## Resumo

- Campos: 8
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| DatAlt | Date | Sim | Data da Reestruturação do Organograma |
| NomTab | String(020) | Sim | Nome da Tabela de Usuário |
| NomOrg | String(020) | Sim | Nome do campo do Organograma |
| NomLoc | String(020) | Sim | Nome do campo de Local |
| NomDat | String(020) | Sim | Nome do campo de Data Alteração/Início |
| NomExt | String(020) | Sim | Nome do campo de Data Extinção/Término |
| TipTra | Number(001,0) | Sim | Tratamento para a tabela na Reestruturação do Organograma |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016TAB_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

