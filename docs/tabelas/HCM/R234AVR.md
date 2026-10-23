# R234AVR

## Descrição

Evento - Avaliação de Eficácia - Respostas

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CodTst | String(005) | Não | Código do Teste |
| CodPer | String(003) | Não | Código da Pergunta |
| CodRes | String(002) | Sim | Código da Resposta |
| DesRes | String(1000) | Sim | Registrar a resposta subjetiva |

---

## Chave Primária

- CodEvn
- CodPes
- CodTst
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234AVR_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234AVR_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R234AVR_002

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_R234AVR_003

**Tabela:** R136PER

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |

