# R136RES

## Descrição

Testes Turma - Respostas

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTst | String(005) | Não | Código do Teste |
| CodPer | String(003) | Não | Código da Pergunta |
| CodRes | String(002) | Não | Código da Resposta |
| DesRes | String(500) | Sim | Descrição da Resposta |
| ResEqv | String(030) | Sim | Abrangência das Resposta Equivalentes |
| ResCor | String(001) | Sim | Reposta Correta |

---

## Chave Primária

- CodTst
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R136RES_001

**Tabela:** R136PER

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |

