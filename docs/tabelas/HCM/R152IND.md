# R152IND

## Descrição

Tabela de detalhe de pendência de indisponibilidade de equipamento

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| CodDsp | Number(009,0) | Não | Código do dispositivo |
| DatInd | Date | Não | Data da indisponibilidade do dispositivo |
| HorInd | Number(005,0) | Não | Hora da indisponibilidade do dispositivo |
| JSON | String(4000) | Sim | JSON do evento de georreferenciamento |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

### R152INDIndice2

**Tipo:** Não unico

Campos:
- CodDsp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
