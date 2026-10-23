# R058IED

## Descrição

Informações Extensíveis do Dispositivo

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| IdtIed | String(020) | Não | Identificador Informação Extensível |
| TieDsp | Number(001,0) | Sim | Tipo Informação Extensível |
| InfExt | String(512) | Sim | Dado Informação Extensível |

---

## Chave Primária

- CodDsp
- IdtIed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058IED_000

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

