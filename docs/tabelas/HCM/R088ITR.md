# R088ITR

## Descrição

Tabela de Infrações de Trânsito

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInf | String(005) | Não | Código da Infração de Trânsito |
| DesInf | String(080) | Sim | Descrição da Infração de Trânsito |
| EnqCtb | String(020) | Sim | Enquadramento no Código de Trânsito Brasileiro |
| GraInf | Number(001,0) | Sim | Gravidade da Infração |
| RspInf | String(020) | Sim | Responsabilidade pela Infração |
| CmpInf | String(020) | Sim | Competência da Infração |
| QtdPon | Number(002,0) | Sim | Quantidade de Pontos da Infração |
| ValUFR | Number(011,2) | Sim | Valor da Infração |
| DesPen | String(500) | Sim | Descrição da Penalidade |

---

## Chave Primária

- CodInf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
