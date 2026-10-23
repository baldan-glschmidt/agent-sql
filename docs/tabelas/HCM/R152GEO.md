# R152GEO

## Descrição

Tabela de detalhe de pendência do evento Georreferenciamento

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| CodDsp | Number(009,0) | Sim | Código do dispositivo |
| VerPlf | Number(003,0) | Sim | Versão do plano de localização física |
| CodPlf | Number(007,0) | Sim | Código do local físico |
| JSON | String(4000) | Sim | JSON do evento de georreferenciamento |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

### R152GEOIndice2

**Tipo:** Não unico

Campos:
- CodDsp

### R152GEOIndice3

**Tipo:** Não unico

Campos:
- VerPlf
- CodPlf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
