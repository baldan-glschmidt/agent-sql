# R062DSP

## Descrição

Alarmes do Dispositivo

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| TipAlm | Number(002,0) | Sim | Tipo do Alarme |
| CodSin | Number(003,0) | Não | Código do Sinal de Alarme |
| CodRac | Number(003,0) | Sim | Código da Reação |

---

## Chave Primária

- CodDsp
- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R062DSP_004

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

