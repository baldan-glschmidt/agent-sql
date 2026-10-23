# R152ACV

## Descrição

Tabela de detalhe de pendência do evento Controle de Acesso de Veículo

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| SeqReg | Number(017,0) | Sim | Código sequencial da marcação de acesso em recinto alfandegado |
| CodPlt | Number(005,0) | Sim | Código do site da marcação de acesso em recinto alfandegado |
| JSON | String(4000) | Sim | JSON do evento de Controle de Acesso de Veículos |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

### R152ACVIndice2

**Tipo:** Não unico

Campos:
- SeqReg
- CodPlt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
