# R058FVV

## Descrição

Cadastro da faixa de acesso de veículos

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| FaiLPR | Number(003,0) | Não | Código da Faixa Horária de Validação de Veículo |
| SeqFai | Number(001,0) | Não | Sequência da Faixa Horária de Validação de Veículos |
| IniFai | Number(005,0) | Sim | Início da Faixa Horária |
| FimFai | Number(005,0) | Sim | Fim da Faixa Horária |
| FVVDiN | Number(001,0) | Sim | Tipo Validação LPR na Faixa - Dias Normais |
| FVVSab | Number(001,0) | Sim | Tipo Validação LPR na Faixa - Sábado |
| FVVDom | Number(001,0) | Sim | Tipo Validação LPR na Faixa - Domingo |
| FVVFer | Number(001,0) | Sim | Tipo Validação LPR na Faixa - Feriado |

---

## Chave Primária

- FaiLPR
- SeqFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058FVV_000

**Tabela:** R058FVE

| Origem | Destino |
|--------|---------|
| FaiLPR | FaiLPR |

