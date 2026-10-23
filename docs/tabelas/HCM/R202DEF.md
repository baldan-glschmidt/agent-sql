# R202DEF

## Descrição

Definições - Testes Certificação

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| ResAle | String(001) | Sim | Define se as respostas do Teste serão geradas de forma aleatória |
| ResCor | String(001) | Sim | Informa a quantidade de respostas corretas no teste |
| ArqHte | String(001) | Sim | Apresentar link para o arquivo da hab. técnica na lista de testes autorizados |
| NomMod | String(011) | Sim | Modelo de Relatório na tela de Resultado do Teste (WEB) |
| UsaNiv | String(001) | Sim | Define se utiliza Níveis de Dificuldade nos testes |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R202DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

