# R076DEN

## Descrição

Definição Enquadramento

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipSis | Number(002,0) | Não | Tipo Sistema |
| EstCar | Number(004,0) | Não | Código da Estrutura do Cargo |
| CodCar | String(024) | Não | Código do Cargo |
| DprAva | Number(001,0) | Sim | Data das Propostas Avaliações |
| PdcMin | Number(005,2) | Sim | Limite Mínimo % Desempenho |
| PdcMax | Number(005,2) | Sim | Limite Máximo % Desempenho |
| MesCpl | Number(002,0) | Sim | Número de Meses Complemento |
| MotPro | Number(003,0) | Sim | Motivo Alteração Cargo |
| CodMot | Number(003,0) | Sim | Motivo do Enquadramento |
| UsaAvl | String(001) | Sim | Usa Avaliação(S,N) |

---

## Chave Primária

- TipSis
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076DEN_008

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

