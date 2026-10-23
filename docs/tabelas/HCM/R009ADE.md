# R009ADE

## Descrição

Assinatura Espelho de Ponto - Definições

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
| CodDAD | Number(002,0) | Não | Código Definição Assinatura Digital |
| DesDAD | String(040) | Sim | Descrição |
| DiaAss | Number(002,0) | Sim | Dias para Assinatura |
| ModRel | String(020) | Sim | Modelo de Relatório Espelho de Ponto |
| BloAce | String(001) | Sim | Bloquear Acerto com Assinatura Pendente |
| PerCan | String(001) | Sim | Permite Cancelar Assinatura |
| DiaCan | Number(002,0) | Sim | Dias Úteis Cancelar Assinatura |
| NotVen | Number(003,0) | Sim | Notifica Assinaturas Vencidas para Gestores |
| NotCol | Number(003,0) | Sim | Notifica Pendencias para Colaborador |
| NofCfm | Number(003,0) | Sim | Notifica Confirmação Assinatura |
| NotRep | Number(003,0) | Sim | Notifica Reprovação Assinatura |

---

## Chave Primária

- CodDAD

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
