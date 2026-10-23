# R040PCC

## Descrição

Publicação Recibo de Férias - Campos customizados

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRel | String(020) | Não | Modelo de Relatório Customizado |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| SeqCmp | Number(002,0) | Não | Sequencia do Registro |
| NomCmp | String(010) | Sim | Nome do Campo Customizado |
| DesCmp | String(255) | Sim | Descrição do Campo |

---

## Chave Primária

- ModRel
- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer
- SeqCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
