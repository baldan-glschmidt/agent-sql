# E027STR

## Descrição

Tabelas - Situações Tributárias

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodStr | String(003) | Não | Código interno da situação tributária |
| DesStr | String(250) | Não | Descrição da situação tributária |
| AbrStr | String(060) | Não | Abreviatura da situação tributária |
| CodCrt | Number(001,0) | Sim | Código do regime tributário associada a situação tributária |
| CodMsg | Number(004,0) | Sim | Código da mensagem relacionada a situação tributária |
| CodPdv | Number(004,0) | Sim | Código interno no PDV |
| ForEsc | String(001) | Sim | Forma de escrituração para não tributadas |
| StrSit | String(001) | Sim | Situação tributária PAF/ECF |
| CodCst | String(003) | Sim | Situação tributária no varejo |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |

---

## Chave Primária

- CodStr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
