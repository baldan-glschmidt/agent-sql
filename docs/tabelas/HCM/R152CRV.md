# R152CRV

## Descrição

Tabela de detalhe de pendência do evento Credenciamento de Veículos

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data de início do uso do crachá |
| HorIni | Number(005,0) | Não | Hora de início do uso do crachá |
| JSON | String(4000) | Sim | JSON do evento de Credenciamento de Veículos |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
