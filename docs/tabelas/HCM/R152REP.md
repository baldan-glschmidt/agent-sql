# R152REP

## Descrição

Tabela de detalhe de pendência do evento Representantes

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| DatIni | Date | Sim | Data de início do uso do crachá |
| HorIni | Number(005,0) | Sim | Hora de início do uso do crachá |
| SeqEnt | Number(002,0) | Sim | Sequência do registro - crachá de Visitante |
| JSON | String(4000) | Sim | JSON do evento de Representantes |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

### R152REPIndice2

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc

### R152REPIndice3

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- DatIni
- HorIni
- SeqEnt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
