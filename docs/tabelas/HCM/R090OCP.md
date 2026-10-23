# R090OCP

## Descrição

Incidentes na Portaria

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site do Incidente |
| DatOcP | Date | Não | Data do Incidente na Portaria |
| HorOcP | Number(005,0) | Não | Hora do Incidente na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência do Incidente na Portaria |
| NumAmb | Number(009,0) | Sim | Ambiente de Incidente |
| TipOcP | Number(003,0) | Sim | Tipo do Incidente na Portaria |
| ObsOcP | String(1500) | Sim | Descrição do Incidente na Portaria |
| EccOcp | String(254) | Sim | Endereço Cópia do E-mail para Comunicação a Terceiros |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| IncEnv | Number(001,0) | Sim | Tipo de envolvido no incidente |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090OCP_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R090OCP_005

**Tabela:** R090TOP

| Origem | Destino |
|--------|---------|
| TipOcP | TipOcP |

